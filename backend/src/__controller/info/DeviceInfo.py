import torch
from src.controller.info.GPUInfo import GPUInfo


class DeviceInfo():

    """_summary_
    """

    def __init__(self):
        self.cuda_available = torch.cuda.is_available()
        self.gpus = []

        if self.cuda_available:
            self.num_gpus = torch.cuda.device_count()
            for i in range(self.num_gpus):
                device_name = torch.cuda.get_device_name(i)
                device_props = torch.cuda.get_device_properties(i)
                gpu = GPUInfo(
                    id=i,
                    name=device_name,
                    total_memory=device_props.total_memory,
                    multi_processor_count=device_props.multi_processor_count,
                    regs_per_multiprocessor=device_props.regs_per_multiprocessor,
                    max_threads_per_multi_processor=device_props.max_threads_per_multi_processor
                )
                print(gpu)
                self.gpus.append(gpu)
        else:
            self.num_gpus = 0

    def reset(self):
        """_summary_
        """
        self.__init__()
        pass

    def is_cuda_available(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.cuda_available

    def get_num_gpus(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_gpus

    def get_gpu(self, gpu_id) -> GPUInfo:

        if gpu_id < 0 or gpu_id >= self.num_gpus:
            raise ValueError("Invalid device ID")
        return self.gpus[gpu_id]

    def get_all_gpus(self):
        return self.gpus
