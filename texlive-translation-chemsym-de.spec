Name:		texlive-translation-chemsym-de
Version:	23804
Release:	1
Summary:	German version of chemsym
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/chemsym/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-chemsym-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-chemsym-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the chemsym documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-chemsym-de/00Liesmich.chs
%doc %{_texmfdistdir}/doc/latex/translation-chemsym-de/chemsym-de.dtx
%doc %{_texmfdistdir}/doc/latex/translation-chemsym-de/chemsym-de.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
