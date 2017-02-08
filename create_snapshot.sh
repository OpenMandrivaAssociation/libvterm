git clone https://github.com/neovim/libvterm.git
pushd libvterm
git archive --format=tar --prefix libvterm-0-$(date +%Y%m%d)/ HEAD | xz -vf > ../libvterm-0-$(date +%Y%m%d).tar.xz
popd
