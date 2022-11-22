import pandas as pd
import shutil

exc_file = pd.read_csv('D:/hatt6/video/train/train/label.csv')
real_mp4 = exc_file.loc[exc_file['liveness_score'] == 1]
fake_mp4 = exc_file.loc[exc_file['liveness_score'] == 0]
path_out = 'D:/hatt6/video/train/train/videos/'
path_in = 'D:/hatt6/video/train/train/videos/'
def move_file(Arg1, Arg2):
    for each_vid in Arg1['fname']:
        path_0 = path_out + each_vid
        path_1 = path_in + Arg2 + '/' + each_vid
        shutil.move(path_0, path_1)
move_file(real_mp4,'Real')
move_file(fake_mp4,'Fake')