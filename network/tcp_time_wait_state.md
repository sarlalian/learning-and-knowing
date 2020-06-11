

tcp_tw_reuse - INTEGER
	Enable reuse of TIME-WAIT sockets for new connections when it is
	safe from protocol viewpoint.
	0 - disable
	1 - global enable
	2 - enable for loopback traffic only
	It should not be changed without advice/request of technical
	experts.
	Default: 2


tcp_tw_recycle - INTEGER
    Removed in recent kernels


The lack of documentation on the tw_XXX sysctls makes it so that numerous tuning
guides advise setting both to 1 to reduce the number the number of sockets in the
TIME-WAIT state. 

However, as stated by tcp(7) manual page, the net.ipv4.tcp_tw_recycle option
causes problems for public-facing servers as it won’t handle connections from
two different computers behind the same NAT.



