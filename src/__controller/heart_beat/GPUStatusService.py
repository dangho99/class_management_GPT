from src.utils.log import get_logger
from src.controller.info.DeviceInfo import DeviceInfo
from src.controller.heart_beat.ABC.StatusServiceAbstract import StatusServiceAbstract
from src.utils.ErrorCodeFactory import ErrorCodeFactory


class GPUStatusService(StatusServiceAbstract):
    """_summary_

    Args:
        HeartBeat (_type_): _description_
    """

    def __init__(self) -> None:

        self.logger = get_logger(self.__class__.__name__)
        self.device_info = DeviceInfo()
        super().__init__()
        pass

    def check_all_gpus(self) -> dict:
        """_summary_
        """

        self.logger.info('begin checking all gpus')
        num_gpus = self.device_info.get_num_gpus()
        self.device_info.reset()
        result = self.default_error_result.copy()

        if not self.device_info.cuda_available:
            result['error_code'], result['error_message'] = ErrorCodeFactory()\
                .get_error_code(1)
            self.logger.info('check all gpus successfully')
            return result

        status = False

        for id in range(num_gpus):
            status = status | self.check_gpu(id).get('status')

        if not  status :
            result['error_code'], result['error_message'] = ErrorCodeFactory()\
                .get_error_code(3)
            self.logger.info('check all gpus successfully')
            return result
        self.logger.info('check all gpus successfully')
        return self.default_success_result.copy()

    def check_gpu(self, id: int) -> dict:
        """_summary_
        """
        self.logger.info("begining checking gpu : id=%s", id)
        self.device_info.reset()
        result = super().default_error_result.copy()

        if not self.device_info.cuda_available:
            result['error_code'], result['error_message'] = ErrorCodeFactory().get_error_code(
                1)
            self.logger.info(f'check gpu :{id=} successfully')
            return result

        gpu = self.device_info.get_gpu(id)
        utilization = gpu.get_utilization()

        if utilization.get('memory') is None or utilization.get('gpu') is None:
            self.logger.error("%s", utilization.get('error'))
            result['error_code'], result['error_message'] = ErrorCodeFactory().get_error_code(
                3)
            return result

        if utilization.get('memory') >= 0.9:
            self.logger.warn(
                "The GPU %s had memory usage over 90%", f"(gpu.id)")
            self.logger.info(gpu)

        if utilization.get('gpu') >= 0.9:
            self.logger.warn(f"The GPU({gpu.id}) had usage over 90%")
            self.logger.info(gpu)

        result = self.default_success_result.copy()

        self.logger.info(f'check gpu :{id=} successfully')

        return result

    def heart_beat(self):
        return self.check_all_gpus()
