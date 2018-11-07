
Name:     multimon-ng
Version:  1.1.6
Release:  1
Summary:  Software modem to several digital transmission modes
License:  GPLv2
URL:      https://github.com/EliasOenal/multimon-ng

%global commit 46c3b0a88fd58642e0350af7cc5d4e56aec89d13
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Source0:  https://github.com/EliasOenal/multimon-ng/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires: cmake

%description
multimon-ng is the successor of multimon. It decodes the following digital
transmission modes: POCSAG512 POCSAG1200 POCSAG2400 FLEX EAS UFSK1200 CLIPFSK 
AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 
ZVEI3 DZVEI PZVEI EEA EIA CCIR MORSE CW X10

%prep
echo %{Source0}
%autosetup -n multimon-ng-%{commit}

%build
%cmake .
%make_build

%install
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%{_bindir}/multimon-ng

%doc README.md
%license COPYING

%changelog
* Wed Nov 07 2018 Doug1 <doug1@github.com> - 1.1.6-1
- Initial version of the package
