from omegaconf import OmegaConf as OC

def GetConf(path: str = './conf.yaml'):
    return OC.load(path)
