Name:		rsec
Version:	0.70.1
Release:	4

Summary:	Security Reporting tool
License:	GPLv2
Group:		System/Base
URL:		http://annvix.org/Tools/rsec
Source0:	http://annvix.org/downloads/rsec/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	bash
Requires:	coreutils
Requires:	perl-base
Requires:	diffutils
Requires:	shadow-utils
Requires:	gawk
Requires:	mailx
Requires:	setup >= 2.2.0-21mdk
Requires:	iproute2
Requires:	rkhunter >= 1.3.0
Conflicts:	passwd < 0.67
Conflicts:	msec

%description
The Annvix Security Reporting tool (rsec) is largely based on the
Mandriva Linux msec program.  rsec produces the same reports as msec, but
does not manage permission issues or system configuration changes.  It is
nothing more than a reporting tool to advise you of changes to your system
and potential problem areas.  Any changes or fixes are entirely up to the
user to correct.


%prep
%setup -q


%build
make CFLAGS="%{optflags}"


%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
%makeinstall_std

pushd %{buildroot}%{_sysconfdir}/cron.daily
    ln -s ../..%{_datadir}/rsec/pkgcheck.sh pkgcheck
popd


%post
touch /var/log/security.log && chmod 0640 /var/log/security.log


%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/promisc_check
%{_bindir}/rsec_find
%dir %_datadir/rsec
%{_datadir}/rsec/*
%{_mandir}/man8/rsec.8*
%dir %attr(0750,root,root) /var/log/security
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/security/rsec.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/rsec
%config(noreplace) %{_sysconfdir}/cron.daily/rsec
%config(noreplace) %{_sysconfdir}/cron.hourly/rsec
%{_sysconfdir}/cron.daily/pkgcheck
%ghost %attr(0640,root,root) /var/log/security.log


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.70.1-3mdv2010.0
+ Revision: 433457
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.70.1-2mdv2009.0
+ Revision: 269223
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Vincent Danen <vdanen@mandriva.com> 0.70.1-1mdv2009.0
+ Revision: 202141
- import rsec


