import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 as cv
from scipy.spatial.distance import pdist, squareform
from sklearn.decomposition import PCA, KernelPCA as KPCA, SparsePCA as SPCA
from sklearn.preprocessing import normalize
import torch
import torchvision as tv
from torchvision.models import vgg19 as vgg

from params import *


class Video():

    def __init__(self, video, matrix=False):

        self.video = video
        self.features = pd.read_csv(FEATURES_PATH+video+'.csv').to_numpy()
        self.truth = pd.read_csv(TRUTH_PATH+video+'.csv').to_numpy()
        self.matrix = None

        if matrix:
            self.matrix = calcDistanceMatrix(self.features)


def getImgFeature(img, extractor, device=torch.device('cpu')):

    extractor.eval()
    trans = tv.transforms.Compose([
        tv.transforms.Resize((224, 224)),
        tv.transforms.ToTensor()
    ])

    img = trans(img)
    img = img.unsqueeze(0).to(device)
    out = extractor(img)

    if out.device.type != 'cpu':
        out = out.to(torch.device('cpu'))

    return out.detach().numpy().ravel()


def compareFeatures(h1, h2):
    return


def getImgSaliency(img):
    return


def calcDistanceMatrix(m):
    cor = pdist(m)
    cor = squareform(cor)
    cor = normalize(cor)
    return cor


def action(action, data, param):

    if action == 'PCA':
        pca = PCA(
            n_components=param['n_components']*min(data.shape),
            svd_solver=param['svd_solver'],
            copy=True
        )
        pca.fit(data)
        out = pca.transform(data)
        return out

    elif action == 'KPCA':
        kpca = KPCA(
            n_components=param['n_components']*min(data.shape),
            kernel=param['kernel'],
            # gamma=param['gamma']*(1/data.shape[1]),
            degree=param['degree'],
            coef0=param['ceof0'],
            # eigen_solver=param['eigen_solver'],
            copy_X=True,
            n_jobs=-1
        )
        kpca.fit(data)
        out = kpca.transform(data)
        return out

    elif action == 'SPCA':
        spca = SPCA(
            n_components=param['n_components']*min(data.shape),
            alpha=param['alpha'],
            # ridge_alpha=param['ridge_alpha'],
            max_iter=param['max_iter'],
            n_jobs=-1
        )
        spca.fit(data)
        out = spca.transform(data)
        return out

    elif action == 'MDS':
        return

    elif action == 'SNE':
        return


if __name__ == '__main__':
    pass
