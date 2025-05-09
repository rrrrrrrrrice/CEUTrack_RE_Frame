from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
        settings = EnvSettings()
        # settings.coesot_path = '/wangx/DATA/Dataset/COESOT'
        settings.fe108_path = '/rydata/dataset/FE240'
        settings.network_path = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/output'    # Where tracking networks are stored.
        settings.prj_dir = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision'
        settings.result_plot_path = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/output'
        settings.results_path = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/output'    # Where to store tracking results
        settings.save_dir = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/output'
        settings.segmentation_path = '/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/output'
        #settings.visevent_path = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/VisEvent'
        #settings.visevent_path = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c01/DATA/chenqiang/COESOT/data/VisEvent'
        return settings

