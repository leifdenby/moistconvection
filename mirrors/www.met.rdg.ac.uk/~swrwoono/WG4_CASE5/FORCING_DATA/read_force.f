      PROGRAM read_force
      
      IMPLICIT NONE

      INTEGER nlevs ! number of vertical levels in forcing data
      PARAMETER (nlevs=41)

      INTEGER ntime ! number of time levels in forcing data
      PARAMETER (ntime=49)      ! 4*ndays+1 where 
                                ! ndays = length of integration in days
      
      REAL time(ntime)          ! time since start of integration (hours)
      REAL sst(ntime)           ! SST (K)
      REAL pr(nlevs,ntime)       ! Pressure (mb)
      REAL sthls(nlevs,ntime)   ! Large-scale forcing of Pot. Temp (K/day)
      REAL sqls(nlevs,ntime)    ! Large-scale forcing of q (g/kg/day)
      REAL u(nlevs,ntime)       ! Zonal wind (m/s)
      REAL v(nlevs,ntime)       ! Meridional Wind (m/s)
      REAL w(nlevs,ntime)       ! Veritcal pressure velocity (Pa/s)
      
      INTEGER iy,im,id,ih       ! Year, month, day, hour
      INTEGER k,p               ! Loop counters

      CHARACTER*20 fname

      fname='a0_force.dat'


      OPEN(31,file=fname,status='old')

      DO p=1,ntime

         READ(31,'(f5.1,f8.2,4i7)') time(p),sst(p),iy,im,id,ih
         
         DO k=1,nlevs
            READ(31,'(F7.1,2e12.4,2F7.2,e12.4)') pr(k,p),sthls(k,p),
     +           sqls(k,p),u(k,p),v(k,p),w(k,p)
         ENDDO
      ENDDO

      END
