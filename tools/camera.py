from abc import ABC, abstractmethod

class Camera(ABC):
    def __init__(self) -> None:
        self.isRunning = False
        self.cam = None

        self.params = {}
        self.lastFrame = None

    def __del__(self) -> None:
        self.isRunning = False
    
    @abstractmethod
    def get_list_of_cameras(self) -> list:
        pass
    
    @abstractmethod
    def pick_camera(self, index) -> None:
        pass
    
    @abstractmethod
    def cam_info(self) -> str:
        pass

    @abstractmethod
    def get_image(self): #numpy array
        pass



    @abstractmethod
    def init_parameters(self) -> None:
        pass

    def get_parameters(self) -> dict:
        return self.params
    
    def set_parameters(self, params : dict) -> int:
        for key, value in params.items():
            if self.params.get(key) == None:
                print(f'Warning! Parameter "{key}" is invalid.')
                return 1
            else:
                if self.params[key]['min'] <= value <= self.params[key]['max']:
                    self.params[key]['value'] = value
                    self.update_param(key)
                    return 0
                else:
                    print(f'Warning! Parameter "{key}" is out of range: '
                          f'[{self.params[key]["min"]}; {self.params[key]["max"]}]')
                    return 1

    @abstractmethod
    def update_param(self, key) -> int:
        pass



    def run(self) -> None:
        self.isRunning = True
        
    def stop(self) -> None:
        self.isRunning = False
    