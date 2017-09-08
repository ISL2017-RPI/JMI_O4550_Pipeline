import sys
import JMI_O4550
import numpy as np

def JMI(data_file, target_file, hm_feat):
    my_JMI = JMI_O4550.initialize()
    feat = my_JMI.JMI_primitive_O4550(data_file, target_file, hm_feat)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    hm_feat = 10
    selected_feature = np.array(JMI(data, target, hm_feat), dtype=np.int16)
    np.savetxt('Features_O4550_JMI.csv', selected_feature, delimiter=',')
    print selected_feature