Summary:	Application-Level Forward Erasure Correction codes
Summary(pl.UTF-8):	Kody korygujące dla usuniętych informacji działające w warstwie aplikacji
Name:		openfec
Version:	1.4.2
%define	tagver	%(echo %{version} | tr . _)
Release:	1
License:	CeCILL-C
Group:		Libraries
#Source0Download: http://openfec.org/downloads.html
Source0:	http://openfec.org/files/%{name}_v%{tagver}.tgz
# Source0-md5:	c4f8b0aa3e9352f2e713e3db2885ea1c
Patch0:		%{name}-opt.patch
URL:		http://openfec.org/
BuildRequires:	cmake >= 2.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenFEC library implements Application-Level Forward Erasure
Correction codes, or AL-FEC (also called UL-FEC, for Upper-Layers
FEC). The idea, in one line, is to add redundancy in order to be able
to recover from erasures. Because of their position in the
communication stack, these codes are implemented as software codecs,
and they find many applications in robust transmission and distrituted
storage systems.

%description -l pl.UTF-8
Biblioteka OpenFEC implementuje kody korygujące dla usuniętych
informacji działające w warstwie aplikacji (AL-FEC, UL-FEC -
Application-Level Forward Erasure Correction, Upper-Layers Forward
Erasure Correction). Idea to w skrócie dodanie redundancji, aby
umożliwić odtworzenie usuniętych informacji. Ze względu na położenie w
stosie komunikacyjnym kody te są zaimplementowane jako programowe
kodeki, mające zastosowanie w mocnych systemach transmisji i
przechowywania danych.

%package devel
Summary:	Header files for OpenFEC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenFEC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenFEC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenFEC.

%prep
%setup -q -n %{name}_v%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
install -d $RPM_BUILD_ROOT%{_includedir}/openfec/{lib_advanced/ldpc_from_file,lib_common,lib_stable/{2d_parity_matrix,ldpc_staircase,reed-solomon_gf_2_{8,m}}}

install bin/PLD/eperftool $RPM_BUILD_ROOT%{_bindir}
cp -a bin/PLD/libopenfec.so* $RPM_BUILD_ROOT%{_libdir}

cp -p src/lib_advanced/ldpc_from_file/{of_codec_profile,of_ldpc_ff_api}.h $RPM_BUILD_ROOT%{_includedir}/openfec/lib_advanced/ldpc_from_file
cp -p src/lib_common/{of_debug,of_mem,of_openfec_api,of_openfec_profile,of_types}.h $RPM_BUILD_ROOT%{_includedir}/openfec/lib_common
cp -p src/lib_stable/2d_parity_matrix/{of_2d_parity_api,of_codec_profile}.h $RPM_BUILD_ROOT%{_includedir}/openfec/lib_stable/2d_parity_matrix
cp -p src/lib_stable/ldpc_staircase/{of_codec_profile,of_ldpc_staircase_api}.h $RPM_BUILD_ROOT%{_includedir}/openfec/lib_stable/ldpc_staircase
cp -p src/lib_stable/reed-solomon_gf_2_8/{of_codec_profile,of_reed-solomon_gf_2_8_api}.h $RPM_BUILD_ROOT%{_includedir}/openfec/lib_stable/reed-solomon_gf_2_8
cp -p src/lib_stable/reed-solomon_gf_2_m/{of_codec_profile,of_reed-solomon_gf_2_m_api}.h $RPM_BUILD_ROOT%{_includedir}/openfec/lib_stable/reed-solomon_gf_2_m

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENCE_CeCILL-C_V1-en.txt Licence_CeCILL_V2-en.txt README
%attr(755,root,root) %{_bindir}/eperftool
%attr(755,root,root) %{_libdir}/libopenfec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenfec.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenfec.so
%{_includedir}/openfec
