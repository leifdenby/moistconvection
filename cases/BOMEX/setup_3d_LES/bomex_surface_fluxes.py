# coding: utf-8

Rd = 287.05
Rv= 461.51
qv = 17.0e-3
qd = 1.0 - qv
R = qv*Rv + qd*Rd
p = 101500
T = 300.4
p/T*1.0/R
R
cp_d = 1005.46
cp_v = 1859.0
cp = qd*cp_d + qv*cp_v
rho = p/T*1.0/R
cp*rho*8.0e-3
8.0e-3*cp
Lv = 2.5008e6
rho*Lv*5.2e-5
cp_d*rho*8.0e-3
cp_d*p/T/Rd*8.0e-3
