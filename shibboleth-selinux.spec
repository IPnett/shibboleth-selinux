%define _prefix   /

Name:		shibboleth-selinux	
Version:	1.0.0
Release:	8%{?dist}
Summary:	SELinux Policy for shibboleth

Group:		System Environment/Base
BuildArch:	noarch
License:	GPLv2
Requires:		policycoreutils, libselinux-utils
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):	policycoreutils
BuildRequires:		selinux-policy selinux-policy-devel
Source0: 		./shibboleth.pp
Source1: 		./shibd_selinux.8.gz


%description
SELinux Policy module for use with shibboleth


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/shibboleth/shibboleth.pp
install -D %{S:1} %{buildroot}%{_prefix}/usr/share/man/man8/shibd_selinux.8.gz


%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/shibboleth/
%attr(0600, root, root) /usr/share/selinux/packages/shibboleth/shibboleth.pp
%attr(0644, root, root) /usr/share/man/man8/shibd_selinux.8.gz

%post
	/usr/sbin/semodule -i /usr/share/selinux/packages/shibboleth/shibboleth.pp 
	restorecon -R /sbin/shibd /var/log/shibboleth /var/run/shibboleth /var/cache/shibboleth /etc/shibboleth

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/semodule -r shibboleth
	restorecon -R /sbin/shibd /var/log/shibboleth /var/run/shibboleth /var/cache/shibboleth /etc/shibboleth
fi


%changelog

