__author__ = 'amrit'
import operator
import numpy as np

score1 = {8: {1: {0.3: [[23, 0.7887233511355132, 0.0938595867742349], [25, 0.22876222127045265, 0.9452706955539223],
                        [21, 0.9391491627785106, 0.38120423768821243], [14, 0.43788759365057206, 0.49581224138185065],
                        [15, 0.49543508709194095, 0.4494910647887381], [10, 0.8357651039198697, 0.43276706790505337],
                        [25, 0.22876222127045265, 0.9452706955539223], [28, 0.030589983033553536, 0.0254458609934608],
                        [21, 0.9391491627785106, 0.38120423768821243], [15.3, 0.7163545099344646, 0.12995356792602356]],
                  0.2: [[12, 0.8474337369372327, 0.763774618976614], [15, 0.49543508709194095, 0.4494910647887381],
                        [10, 0.8357651039198697, 0.43276706790505337], [26, 0.0021060533511106927, 0.4453871940548014],
                        [28, 0.030589983033553536, 0.0254458609934608], [14, 0.4221165755827173, 0.029040787574867943],
                        [12, 0.8474337369372327, 0.763774618976614], [23, 0.7887233511355132, 0.0938595867742349],
                        [26, 0.0021060533511106927, 0.4453871940548014],
                        [14, 0.43788759365057206, 0.49581224138185065]]}, 2: {
    0.3: [[12, 0.8474337369372327, 0.763774618976614], [23, 0.7887233511355132, 0.0938595867742349],
          [26, 0.0021060533511106927, 0.4453871940548014], [28, 0.030589983033553536, 0.0254458609934608],
          [12, 0.8474337369372327, 0.763774618976614], [24.5, 0.2688209948131036, 0.013739063174881473],
          [21.7, 0.9794324081874688, 0.34877941407303364], [26, 0.0021060533511106927, 0.4453871940548014],
          [21, 0.9391491627785106, 0.38120423768821243], [10, 0.8357651039198697, 0.43276706790505337],
          [28, 0.030589983033553536, 0.0254458609934608], [14, 0.43788759365057206, 0.49581224138185065]],
    0.2: [[15, 0.49543508709194095, 0.4494910647887381], [10, 0.8357651039198697, 0.43276706790505337],
          [25, 0.22876222127045265, 0.9452706955539223], [21, 0.9391491627785106, 0.38120423768821243],
          [14, 0.4221165755827173, 0.029040787574867943], [14, 0.43788759365057206, 0.49581224138185065],
          [10, 0.8357651039198697, 0.43276706790505337], [25, 0.22876222127045265, 0.9452706955539223],
          [14.8, 0.35016287788159217, 1], [14, 0.4221165755827173, 0.029040787574867943],
          [14, 0.43788759365057206, 0.49581224138185065], [12, 0.8474337369372327, 0.763774618976614],
          [24.5, 0.2688209948131036, 0.013739063174881473], [23, 0.7887233511355132, 0.0938595867742349],
          [26, 0.0021060533511106927, 0.4453871940548014], [25, 0.22876222127045265, 0.9452706955539223],
          [30, 0.4947159855733886, 0.3853020713101883], [14, 0.4221165755827173, 0.029040787574867943]]},
              3: {0.1: [[14, 0.4221165755827173, 0.029040787574867943], [10, 0.8357651039198697, 0.43276706790505337]],
                  0.3: [[23, 0.7887233511355132, 0.0938595867742349], [25, 0.22876222127045265, 0.9452706955539223],
                        [21, 0.9391491627785106, 0.38120423768821243], [14, 0.4221165755827173, 0.029040787574867943],
                        [27.3, 1, 0.4265773971277693], [10, 1, 0.7620235341769263],
                        [10, 0.8357651039198697, 0.43276706790505337], [26, 0.0021060533511106927, 0.4453871940548014],
                        [28, 0.030589983033553536, 0.0254458609934608], [28.0, 0.019550270386055214, 0],
                        [27.8, 0, 0.7589227905973694], [14, 0.43788759365057206, 0.49581224138185065],
                        [23, 0.7887233511355132, 0.0938595867742349], [28.0, 0.14555441028964475, 0.2559253873837718]],
                  0.2: [[15, 0.49543508709194095, 0.4494910647887381], [10, 0.8357651039198697, 0.43276706790505337],
                        [26, 0.0021060533511106927, 0.4453871940548014], [28, 0.030589983033553536, 0.0254458609934608],
                        [14, 0.43788759365057206, 0.49581224138185065], [23, 0.7887233511355132, 0.0938595867742349],
                        [25, 0.22876222127045265, 0.9452706955539223], [11.200000000000001, 1, 0.38372068629519746],
                        [14, 0.43788759365057206, 0.49581224138185065],
                        [12.6, 0.5289129597266544, 0.027815028215086503], [23, 0.7887233511355132, 0.0938595867742349],
                        [10, 0.8357651039198697, 0.43276706790505337], [25, 0.22876222127045265, 0.9452706955539223],
                        [28, 0.030589983033553536, 0.0254458609934608], [21, 0.9391491627785106, 0.38120423768821243],
                        [16.1, 0, 0.7418815664782472], [10.4, 1, 0.6094639580026607], [10, 1, 0.7620235341769263],
                        [26, 0.0021060533511106927, 0.4453871940548014], [25, 0.22876222127045265, 0.9452706955539223],
                        [21, 0.9391491627785106, 0.38120423768821243], [14, 0.4221165755827173, 0.029040787574867943],
                        [14, 0.43788759365057206, 0.49581224138185065]],
                  0.4: [[12, 0.8474337369372327, 0.763774618976614]]}, 4: {
        0.3: [[12, 0.8474337369372327, 0.763774618976614], [25, 0.22876222127045265, 0.9452706955539223],
              [21, 0.9391491627785106, 0.38120423768821243], [14, 0.43788759365057206, 0.49581224138185065],
              [11.9, 0.6685156304744215, 0.24903927550638105], [15, 0.49543508709194095, 0.4494910647887381],
              [10, 0.8357651039198697, 0.43276706790505337], [28, 0.030589983033553536, 0.0254458609934608],
              [12, 0.8474337369372327, 0.763774618976614], [15, 0.49543508709194095, 0.4494910647887381], [13.3, 1, 0],
              [30, 0.8610921923365618, 0.05776560562244624], [15.4, 0.021029064254023178, 0.5196521703413782],
              [28.7, 0.8038011147599253, 1], [28, 0.030589983033553536, 0.0254458609934608],
              [21, 0.9391491627785106, 0.38120423768821243]], 0.1: [[10, 0.8357651039198697, 0.43276706790505337]],
        0.2: [[15, 0.49543508709194095, 0.4494910647887381], [23, 0.7887233511355132, 0.0938595867742349],
              [26, 0.0021060533511106927, 0.4453871940548014], [28, 0.030589983033553536, 0.0254458609934608],
              [14, 0.4221165755827173, 0.029040787574867943], [23, 0.7887233511355132, 0.0938595867742349],
              [26, 0.0021060533511106927, 0.4453871940548014], [25, 0.22876222127045265, 0.9452706955539223],
              [22.5, 0.5327994110224824, 0.4932768021013433], [13.4, 0.8673724877149427, 0.4698156858336756],
              [14, 0.43788759365057206, 0.49581224138185065], [23, 0.7887233511355132, 0.0938595867742349],
              [10, 0.8357651039198697, 0.43276706790505337], [26, 0.0021060533511106927, 0.4453871940548014],
              [25, 0.22876222127045265, 0.9452706955539223], [28, 0.030589983033553536, 0.0254458609934608],
              [21, 0.9391491627785106, 0.38120423768821243], [14, 0.4221165755827173, 0.029040787574867943],
              [12, 0.8474337369372327, 0.763774618976614], [15, 0.49543508709194095, 0.4494910647887381],
              [13.3, 0.5807758931262567, 0.3789592386242525], [15.4, 0.03014378467717499, 0.6250285637206491],
              [25, 0.22876222127045265, 0.9452706955539223], [28, 0.030589983033553536, 0.0254458609934608],
              [21, 0.9391491627785106, 0.38120423768821243], [14, 0.4221165755827173, 0.029040787574867943],
              [14, 0.43788759365057206, 0.49581224138185065], [12, 0.8474337369372327, 0.763774618976614],
              [10, 0.3579157774938228, 0.29684005447674905], [19.0, 0.6607627308621908, 1],
              [26, 0.0021060533511106927, 0.4453871940548014],
              [10.100000000000001, 0.1335122760548857, 0.202976649709397],
              [14, 0.43788759365057206, 0.49581224138185065]]}}, 9: {1: {
    0.1: [[25, 0.4234710877880348, 0.13071891394841717], [13, 0.6777169490132041, 0.9385930756898219],
          [26, 0.3269784217992199, 0.023164898023276592], [11.6, 0.18101543190200026, 1],
          [10, 0.1661345625614383, 0.9526738590904881], [16, 0.3869484713308845, 0.7072904492939808],
          [13, 0.6777169490132041, 0.9385930756898219], [25, 0.8603452927983642, 0.6252371014920886],
          [26, 0.3269784217992199, 0.023164898023276592]],
    0.2: [[23, 0.993165390112413, 0.5880453474090971], [18, 0.8542362875583159, 0.9005878862230072],
          [19, 0.6257599358292166, 0.9855130146576269], [10, 0.6882208082379445, 0.7436355728566928],
          [16, 0.3869484713308845, 0.7072904492939808], [23, 0.15077169692521586, 0.9501217415724769],
          [25, 0.8603452927983642, 0.6252371014920886], [18.4, 0.510248705380326, 0.1781236596377096],
          [25, 0.4234710877880348, 0.13071891394841717], [19, 0.6257599358292166, 0.9855130146576269],
          [23, 0.15077169692521586, 0.9501217415724769]]}, 2: {
    0.1: [[25, 0.4234710877880348, 0.13071891394841717], [16, 0.3869484713308845, 0.7072904492939808],
          [13, 0.6777169490132041, 0.9385930756898219], [23, 0.15077169692521586, 0.9501217415724769],
          [25, 0.8603452927983642, 0.6252371014920886], [26, 0.3269784217992199, 0.023164898023276592],
          [19, 0.6257599358292166, 0.9855130146576269], [10, 0.6882208082379445, 0.7436355728566928],
          [16, 0.3869484713308845, 0.7072904492939808], [13, 0.6777169490132041, 0.9385930756898219],
          [23, 0.15077169692521586, 0.9501217415724769], [25, 0.8603452927983642, 0.6252371014920886],
          [19.4, 0.4554502759312512, 0.5804593828005313], [25, 0.4234710877880348, 0.13071891394841717],
          [16, 0.3869484713308845, 0.7072904492939808], [13, 0.6777169490132041, 0.9385930756898219],
          [26, 0.3269784217992199, 0.023164898023276592]],
    0.2: [[23, 0.993165390112413, 0.5880453474090971], [18, 0.8542362875583159, 0.9005878862230072],
          [19, 0.6257599358292166, 0.9855130146576269], [10, 0.6882208082379445, 0.7436355728566928],
          [23, 0.993165390112413, 0.5880453474090971], [25, 0.4234710877880348, 0.13071891394841717],
          [30, 0.16165467971525183, 0.19314680261822384], [23, 0.993165390112413, 0.5880453474090971],
          [18, 0.8542362875583159, 0.9005878862230072], [14.2, 0.5466186146091172, 0.145279702360246],
          [12.0, 0.6677389705013819, 1], [23, 0.15077169692521586, 0.9501217415724769],
          [25, 0.8603452927983642, 0.6252371014920886]]}, 3: {
    0.1: [[25, 0.4234710877880348, 0.13071891394841717], [26, 0.3269784217992199, 0.023164898023276592],
          [30, 0.29060851257042863, 0.05600885530074009], [10, 0.6882208082379445, 0.7436355728566928],
          [11.0, 1, 0.8925178201051487], [25.7, 0.7004118465879947, 0.6846846913963223],
          [26, 0.3269784217992199, 0.023164898023276592], [25, 0.4234710877880348, 0.13071891394841717],
          [30, 0.44318925732347986, 0.1330315173796967], [10, 0.6882208082379445, 0.7436355728566928],
          [13, 0.6777169490132041, 0.9385930756898219], [15.9, 0.6468840854862363, 0.7341502593054056],
          [26, 0.3269784217992199, 0.023164898023276592], [29.9, 1, 0.54176553017267],
          [25, 0.4234710877880348, 0.13071891394841717], [16, 0.3869484713308845, 0.7072904492939808],
          [23, 0.15077169692521586, 0.9501217415724769], [25, 0.8603452927983642, 0.6252371014920886]],
    0.2: [[23, 0.993165390112413, 0.5880453474090971], [18, 0.8542362875583159, 0.9005878862230072],
          [19, 0.6257599358292166, 0.9855130146576269], [10, 0.6882208082379445, 0.7436355728566928],
          [16, 0.3869484713308845, 0.7072904492939808], [13, 0.6777169490132041, 0.9385930756898219],
          [23, 0.15077169692521586, 0.9501217415724769], [25, 0.8603452927983642, 0.6252371014920886],
          [23, 0.993165390112413, 0.5880453474090971], [18, 0.8542362875583159, 0.9005878862230072],
          [19, 0.6257599358292166, 0.9855130146576269], [16, 0.3869484713308845, 0.7072904492939808],
          [13, 0.6777169490132041, 0.9385930756898219], [18.1, 1, 0.41806344281414987],
          [18, 0.8542362875583159, 0.9005878862230072], [16, 0.3869484713308845, 0.7072904492939808],
          [25, 0.8603452927983642, 0.6252371014920886], [18, 0.8542362875583159, 0.9005878862230072],
          [19, 0.6257599358292166, 0.9855130146576269], [10, 0.6882208082379445, 0.7436355728566928],
          [20.4, 0.2269739242021519, 0.665384511235151], [26, 0.3269784217992199, 0.023164898023276592]]},
                                                                     4: {0.3: [[25.0, 1, 0.6552044764264999]], 0.1: [
                                                                         [10, 0.6882208082379445, 0.7436355728566928],
                                                                         [16, 0.3869484713308845, 0.7072904492939808],
                                                                         [13, 0.6777169490132041, 0.9385930756898219],
                                                                         [26, 0.3269784217992199, 0.023164898023276592],
                                                                         [25.7, 0.050114278088633724, 0],
                                                                         [25, 0.4234710877880348, 0.13071891394841717],
                                                                         [18, 0.8542362875583159, 0.9005878862230072],
                                                                         [10, 0.6882208082379445, 0.7436355728566928],
                                                                         [18.7, 0.9040679034844737,
                                                                          0.45592289223143473],
                                                                         [11.6, 0.35061547765400214,
                                                                          0.8032848698395034],
                                                                         [25, 0.4234710877880348, 0.13071891394841717],
                                                                         [10, 0.6882208082379445, 0.7436355728566928],
                                                                         [16, 0.3869484713308845, 0.7072904492939808],
                                                                         [13, 0.6777169490132041, 0.9385930756898219],
                                                                         [23, 0.15077169692521586, 0.9501217415724769],
                                                                         [25, 0.4234710877880348, 0.13071891394841717],
                                                                         [21.5, 0.32622071600016683,
                                                                          0.34949869111815424],
                                                                         [17.6, 0.12905841871801277, 1],
                                                                         [10, 0.6882208082379445, 0.7436355728566928],
                                                                         [16, 0.3869484713308845, 0.7072904492939808],
                                                                         [11.4, 1, 0.537193487254509],
                                                                         [17.9, 0.6819932526812379,
                                                                          0.7458475263781787]], 0.2: [
                                                                         [23, 0.993165390112413, 0.5880453474090971],
                                                                         [25, 0.4234710877880348, 0.13071891394841717],
                                                                         [18, 0.8542362875583159, 0.9005878862230072],
                                                                         [19, 0.6257599358292166, 0.9855130146576269],
                                                                         [23, 0.15077169692521586, 0.9501217415724769],
                                                                         [25, 0.8603452927983642, 0.6252371014920886],
                                                                         [19, 0.6257599358292166, 0.9855130146576269],
                                                                         [16, 0.3869484713308845, 0.7072904492939808],
                                                                         [25, 0.8603452927983642, 0.6252371014920886],
                                                                         [25.0, 1, 0.6552044764264999],
                                                                         [23, 0.993165390112413, 0.5880453474090971],
                                                                         [18, 0.8542362875583159, 0.9005878862230072],
                                                                         [19, 0.6257599358292166, 0.9855130146576269],
                                                                         [25, 0.8603452927983642, 0.6252371014920886],
                                                                         [25.0, 1, 0.6552044764264999],
                                                                         [23, 0.993165390112413, 0.5880453474090971],
                                                                         [13, 0.6777169490132041, 0.9385930756898219],
                                                                         [23, 0.15077169692521586, 0.9501217415724769],
                                                                         [20.2, 0, 1], [25.0, 1, 0.6552044764264999],
                                                                         [12.0, 0.9946216122908084, 0.9774429485397683],
                                                                         [29.3, 1, 0.5306080039477725],
                                                                         [18, 0.8542362875583159, 0.9005878862230072],
                                                                         [23.5, 0.7982040882054979, 0.8557141457345989],
                                                                         [11.7, 0.8979588982444254, 0.7312736769623533],
                                                                         [13, 0.6777169490132041, 0.9385930756898219],
                                                                         [23, 0.15077169692521586,
                                                                          0.9501217415724769]]}}}
lab=[8,9]
eval=[1,2,3,4]
for l in lab:
    for e in eval:
        for x in score1[l][e].keys():
            k=[]
            al=[]
            beta=[]
            for a in score1[l][e][x]:
                k.append(a[0])
                al.append(a[1])
                beta.append(a[2])
            k_median=np.median(k)
            k_iqr=np.percentile(k,75)-np.percentile(k,25)
            al_median=np.median(al)
            al_iqr=np.percentile(al,75)-np.percentile(al,25)
            beta_median=np.median(beta)
            beta_iqr=np.percentile(beta,75)-np.percentile(beta,25)
            print("k median, k_iqr, almedian, aliqr, bemedian,beiqr",k_median,k_iqr,al_median,al_iqr,beta_median,beta_iqr)