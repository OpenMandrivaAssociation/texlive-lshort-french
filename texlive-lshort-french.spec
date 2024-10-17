Name:		texlive-lshort-french
Version:	23332
Release:	2
Summary:	Short introduction to LaTeX, French translation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-french.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-french.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
French version of A Short Introduction to LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-french/README
%doc %{_texmfdistdir}/doc/latex/lshort-french/historique
%doc %{_texmfdistdir}/doc/latex/lshort-french/lshort-fr-5.01fr-0.tgz
%doc %{_texmfdistdir}/doc/latex/lshort-french/lshort-fr.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
