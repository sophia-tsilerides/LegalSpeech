#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=5:00:00
#SBATCH --mem=2GB
#SBATCH --job-name=get_oyez_mp3s

curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/17-834/17-834_20191016-argument.delivery.mp3 -o 17-834.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-587/18-587_20191112-argument.delivery.mp3 -o 18-587.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-6135/18-6135_20191007-argument.delivery.mp3 -o 18-6135.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-260/18-260_20191106-argument.delivery.mp3 -o 18-260.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1171/18-1171_20191113-argument.delivery.mp3 -o 18-1171.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-938/18-938_20191113-argument.delivery.mp3 -o 18-938.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-6943/18-6943_20191204-argument.delivery.mp3 -o 18-6943.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-280/18-280_20191202-argument.delivery.mp3 -o 18-280.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/17-1498/17-1498_20191203-argument.delivery.mp3 -o 17-1498.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1269/18-1269_20191203-argument.delivery.mp3 -o 18-1269.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1150/18-1150_20191202-argument.delivery.mp3 -o 18-1150.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1116/18-1116_20191204-argument.delivery.mp3 -o 18-1116.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-776/18-776_20191209-argument.delivery.mp3 -o 18-776.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-935/18-935_20191211-argument.delivery.mp3 -o 18-935.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1023/18-1023_20191210-argument.delivery.mp3 -o 18-1023.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-916/18-916_20191209-argument.delivery.mp3 -o 18-916.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1109/18-1109_20191211-argument.delivery.mp3 -o 18-1109.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-7739/18-7739_20191210-argument.delivery.mp3 -o 18-7739.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/17-1712/17-1712_20200113-argument.delivery.mp3 -o 17-1712.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1086/18-1086_20200113-argument.delivery.mp3 -o 18-1086.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1233/18-1233_20200114-argument.delivery.mp3 -o 18-1233.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-882/18-882_20200115-argument.delivery.mp3 -o 18-882.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1059/18-1059_20200114-argument.delivery.mp3 -o 18-1059.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1048/18-1048_20200121-argument.delivery.mp3 -o 18-1048.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-6662/18-6662_20200121-argument.delivery.mp3 -o 18-6662.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1195/18-1195_20200122-argument.delivery.mp3 -o 18-1195.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/17-1268/17-1268_20200224-argument.delivery.mp3 -o 17-1268.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-67/19-67_20200225-argument.delivery.mp3 -o 19-67.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-8369/18-8369_20200226-argument.delivery.mp3 -o 18-8369.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1432/18-1432_20200302-argument.delivery.mp3 -o 18-1432.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1501/18-1501_20200303-argument.delivery.mp3 -o 18-1501.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-7/19-7_20200303-argument.delivery.mp3 -o 19-7.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1323/18-1323_20200304-argument.delivery.mp3 -o 18-1323.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-161/19-161_20200302-argument.delivery.mp3 -o 19-161.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-46/19-46_20200504-argument.delivery.mp3 -o 19-46.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-631/19-631_20200506-argument.delivery.mp3 -o 19-631.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-177/19-177_20200505-argument.delivery.mp3 -o 19-177.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-431/19-431_20200506-argument.delivery.mp3 -o 19-431.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-465/19-465_20200513-argument.delivery.mp3 -o 19-465.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-715/19-715_20200512-argument.delivery.mp3 -o 19-715.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-635/19-635_20200512-argument.delivery.mp3 -o 19-635.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-518/19-518_20200513-argument.delivery.mp3 -o 19-518.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-9526/18-9526_20200511-argument.delivery.mp3 -o 18-9526.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/19-267/19-267_20200511-argument.delivery.mp3 -o 19-267.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-1587/18-1587_20200224-argument.delivery.mp3 -o 18-1584.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2020/18-540/18-540_20201006-argument.delivery.mp3 -o 18-540.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2020/19-71/19-71_20201006-argument.delivery.mp3 -o 19-71.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2020/19-368/19-368_20201007-argument.delivery.mp3 -o 19-368.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2020/19-309/19-309_20201005-argument.delivery.mp3 -o 19-309.mp3
curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2020/18-956/18-956_20201007-argument.delivery.mp3 -o 18-956.mp3
