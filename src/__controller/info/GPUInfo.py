from src.ABC.ObjectAbstract import ObjectAbstract
import pynvml
import torch


class GPUInfo(ObjectAbstract):

    """_summary_
    """

    def __init__(self,
                 id,
                 name,
                 total_memory,
                 multi_processor_count,
                 regs_per_multiprocessor,
                 max_threads_per_multi_processor):

        self.id = id
        self.name = name
        self.total_memory = total_memory
        self.multi_processor_count = multi_processor_count
        self.regs_per_multiprocessor = regs_per_multiprocessor
        self.max_threads_per_multi_processor = max_threads_per_multi_processor

    def get_memory_usage(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if torch.cuda.is_available():
            allocated = torch.cuda.memory_allocated(self.id)
            reserved = torch.cuda.memory_reserved(self.id)
            free = self.total_memory - reserved
            return {
                "allocated": allocated,
                "reserved": reserved,
                "free": free
            }
        else:
            return {
                "allocated": 0,
                "reserved": 0,
                "free": 0
            }

    def get_utilization(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            pynvml.nvmlInit()
            handle = pynvml.nvmlDeviceGetHandleByIndex(self.id)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            return {
                "gpu": utilization.gpu,
                "memory": utilization.memory
            }
        except ImportError:
            return {
                "gpu": None,
                "memory": None,
                "error": f"Import GPU({id}) Error"
            }
        except pynvml.NVMLError as error:
            return {
                "gpu": None,
                "memory": None,
                "error": f"NVMLError -> {str(error)}"
            }

    def __str__(self):
        memory_usage = self.get_memory_usage()
        utilization = self.get_utilization()
        return (f"  GPU {self.id}: {self.name}\n"
                f"  Total Memory: {self.total_memory / (1024 ** 2):.2f} MB\n"
                f"  Multi-Processor Count: {self.multi_processor_count}\n"
                f"  Max Regs per Multiprocessor: {self.regs_per_multiprocessor}\n"
                f"  Max Threads per Multi Processor: {self.max_threads_per_multi_processor}\n"
                f"  Memory Usage: {memory_usage['allocated'] / (1024 ** 2):.2f} MB allocated, "
                f"{memory_usage['reserved'] / (1024 ** 2):.2f} MB reserved, "
                f"{memory_usage['free'] / (1024 ** 2):.2f} MB free\n"
                f"  GPU Utilization: {utilization['gpu']}%, Memory Utilization: {utilization['memory']}%")
