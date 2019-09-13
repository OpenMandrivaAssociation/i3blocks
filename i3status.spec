%define debug_package %{nil}

Summary:	Define blocks for your i3bar status line
Name:		i3blocks
Version:	1.5
Release:	3
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		https://github.com/vivien/i3blocks
Source0:	https://github.com/vivien/i3blocks/archive/%{version}.tar.gz
BuildRequires:	git


%description
Define blocks for your i3bar status line

%prep
%setup -q

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/bash-completion/completions/%{name}
%license COPYING
