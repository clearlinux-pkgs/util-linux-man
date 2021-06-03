Name     : util-linux-man
Version  : 1.4.18
Release  : 107
Source1  : util-linux-man-2.36.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : FSFULLR GPL-3.0 GPL-3.0+
Requires: util-linux-man-man = %{version}-%{release}

%description
man pages for util-linux

%package man
Summary: man components for the util-linux-man package.
Group: Default

%description man
man components for the util-linux-man package.


%prep

%build


%install
export SOURCE_DATE_EPOCH=1615858295
mkdir -p %{buildroot}
pushd %{buildroot}
tar -axf %{SOURCE1}

%files
%defattr(-,root,root,-)


%files man
%defattr(0644,root,root,0755)
/usr/share/man/*
