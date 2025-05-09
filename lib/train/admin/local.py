class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '../../../output/checkpoints'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '../../../output/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/pretrained_models'
        # self.coesot_dir = '/wangx/DATA/Dataset/COESOT/train'
        # self.coesot_val_dir = '/wangx/DATA/Dataset/COESOT/train'
        self.fe108_dir = '/rydata/dataset/FE240/train'
        self.fe108_val_dir = '/rydata/dataset/FE240/train'
        # self.visevent_dir = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c01/DATA/chenqiang/COESOT/data/VisEvent/train'
        # self.visevent_val_dir = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c01/DATA/chenqiang/COESOT/data/VisEvent/test'