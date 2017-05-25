      PROGRAM read_init
      
      IMPLICIT NONE

      INTEGER nlevs
      PARAMETER (nlevs=41)
      
      REAL time                 ! time since start of integration (hours)
      REAL sst                  ! SST (K)
      REAL pr(nlevs)             ! Pressure (mb)
      REAL t(nlevs)             ! Temperature (K)
      REAL q(nlevs)             ! Humidity mixing ratio (g/kg)
      REAL u(nlevs)             ! Zonal wind (m/s)
      REAL v(nlevs)             ! Meridional Wind (m/s)
      
      INTEGER iy,im,id,ih       ! Year, month, day, hour
      INTEGER k                 ! Loop counter

      CHARACTER*20 fname

      fname='a0_init.dat'


      OPEN(31,file=fname,status='old')

      READ(31,'(f5.1,f8.2,4i7)') time,sst,iy,im,id,ih
      
      DO k=1,nlevs
         READ(31,'(F7.1,F9.2,3F8.2)') pr(k),t(k),q(k),u(k),v(k)
      ENDDO
      
      END
