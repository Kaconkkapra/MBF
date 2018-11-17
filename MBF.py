from __future__ import print_function

global fid_bteman
	if len(fid_bteman) != 0:
		i = inputD('[?]Riset Hasil Id Teman/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bteman)
		else:
			os.remove(os.sys.path[0]+'/MBFbteman.txt')
			fid_bteman = []
	return 0
def lanjutG():
	global fid_bgroup
	if len(fid_bgroup) != 0:
		i = inputD('[?]Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bgroup)
		else:
			os.remove(os.sys.path[0]+'/MBFbgroup.txt')
			fid_bgroup = []
	return 0
def menu():
	tampil('''\rh
                     .-.-..
                    /+/++//
                   /+/++//
            \rk*   *\rh /+/++//
             \ /  |/__//
           {\rmX\rh}v{\rmX\rh}|\rcPRX\rh|==========.
             [']  /'|'\           \\
                 /  \  \           '
                 \_  \_ \_    \rk*\rhDragonFly ZomBie
\rk###########################################################
#             \rb*MULTY BRUTEFORCE FACEBOOK*\rk                 #
# \rhBY\rp                                             PIRMANSX \rk#
# \rhGroup FB\rp  https://m.facebook.com/groups/164201767529837 \rk#
# \rhGitHub\rp                     https://github.com/Kaconkkapra/MBF  \rk#
#       \rmDo Not Use This Tool For IllegaL Purpose          \rk#
###########################################################''')
	tampil('''\rk%s\n\rc1 \rhAmbil id dari group\n\rc2 \rhAmbil id dari daftar teman\n\rc3 \rmKELUAR\n\rk%s'''%('#'*20,'#'*20))
	i = inputM('[?]PILIH',[1,2,3])
	if i == 1:
		lanjutG()
		idgroup()
	elif i == 2:
		lanjutT()
		idteman()
	elif i == 3:
		keluar()
bacaData()
menu()
