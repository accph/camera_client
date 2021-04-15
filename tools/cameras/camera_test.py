from tools.camera import Camera
import qimage2ndarray as q2nd
from time import sleep

class CameraTest(Camera):
    def __init__(self) -> None:
        Camera.__init__(self)
        self.cam_list = ['first', 'second']

        self.exposure = 1.
        self.i = 0
        self.N = 40

    def get_list_of_cameras(self) -> list:
        return self.cam_list
    
    def pick_camera(self, index) -> None:
        self.cam = index

    def cam_info(self) -> str:
        if self.cam == None:
            return None
        else:
            return self.cam_list[self.cam]

    def init_parameters(self) -> None:
        self.params = {'exposure' : { 'min' : 0.01, 
                                      'max' : 10, 
                                      'value' : self.exposure } 
                      }

    def update_param(self, key) -> int:
        if key == 'exposure':
            self.exposure = self.params['exposure']['value']
        return 0
    
    def get_image(self): #numpy array
        image = q2nd.imread(f'./test/{self.i}.BMP')
        self.i = (self.i + 1) % self.N

        sleep(self.exposure)
        return self.image
