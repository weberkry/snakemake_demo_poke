mkdir -p logs
unset DRMAA_LIBRARY_PATH

snakemake --jobs 500 \
          --local-cores 24 \
          --resources pdfReport=1 \
          --use-conda \
          --cluster-config cluster_slurm.json \
          --drmaa " -n {threads} \
          --nodes=1 \
          --gres=gpu:tesla:{cluster.gpu} \
          --mem-per-cpu={cluster.mem} \
          -t {cluster.time} \
          -o logs/%x-%j.log" $*

