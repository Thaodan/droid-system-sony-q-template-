%define __find_provides %{nil}
%define __find_requires %{nil}
%define __strip /bin/true
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^.*$
%global debug_package %{nil}

%define habuild_device kirin
%define device i4113

Name:          droid-system-%{habuild_device}-%{device}
Summary:       Built from source /system for Droid HAL adaptations
Version:       0.0.1
Release:       1
Group:         System
License:       Proprietary
Requires:      droid-system-%{habuild_device}
Source0:       %{name}-%{version}.tgz
Source1:       droid-system-%{habuild_device}-rpmlintrc
URL:           https://github.com/mer-hybris/droid-system-sony-ganges-kirin

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

# This section is empty by purpose
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/system
cp %{device}/system/build.prop $RPM_BUILD_ROOT/system/build.prop

%files
%defattr(-,root,root,-)
/system/build.prop
