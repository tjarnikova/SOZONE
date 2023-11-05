import subprocess

subprocess.run(["cdo remapbil,r360x180 /gpfs/data/greenocean/software/resources/MEDUSA/ukesm_allscen_gridT_mld/nemo_cj504o_1m_20920901-20921001_grid-T.nc nemo_cj504o_1m_20920901-20921001_grid-T-rg.nc"]) 
