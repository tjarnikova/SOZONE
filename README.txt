TJSJ - March 2022
tjarnik@gmail.com | T.Jarnikova@uea.ac.uk
UEA Green Ocean Group

Where things are in SOZONE:
**EVAL_forcing**
    ----goal is to understand/evaluate the atmosph. forcing for diff. products----

    *Folder* averaged_forcing
        - the metoffice, era5, ncep forcing, each in their own folder
    *Folder* make_monthly_SO_forcing
        - pyscripts for averaging our work
        - MO_wind_monthly.py > pyscript for averaging winds south of 50
        - runner.ipynb > for running pyscripts (for now)
    *Folder* pkls
        - pkls of the latitude-avgd summer 
        winter hovmollers made in by_latitude_forcing_comparison
    - by_latitude_forcing_comparison > latitudinally averaged hovmollers
    - Forcing_familiarization.ipynb > code scratchpad
    - Mapping_scratchpad.ipynb > figuring out mapping
    - so_landmask.ipynb > update CLQ landmask for our plotting
    - wind_climatology_maps.ipynb > decadal departure from clim, maps
    - wind_zonal_avgs.ipynb > monthly line plots of decadal clim. by zone, 

**RUNS_ANALYSIS**
    - TOM12_TJ_T001_explore > plotting scratchpad
    - Hovmol_Compare_T001_M001.ipynb > comparing our two different runs
    *Folder* pkls
        - pkls of the latitude-avgd summer 
        winter hovmollers made in Hovmol_Compare_T001_M001    


**UTILS**
    ---commonly used functions and landmasks
    -mapfxn.py > code for southern ocean mapping
    -sector_landmask_regrid.nc > sector landmask for regridded prod. 
    -sector_landmask.nc  > landmask for different sectors
            made in EVAL_forcing/so_landmask.ipynb
    - simple_landmask.nc > made in Forcing_familiarization.ipynb, 1 is land 0 is water
    







