# Transfer data from hpc to local machine (run on local machine)

rsync -av --exclude='*.h5ad' -e "ssh -v -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress gw2hpct04:/home/hers_basak/jjiang/jack/outputs/deliverables/6_analysis /c/Users/Chenj/hpc/figures/
