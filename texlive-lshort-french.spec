Name:		texlive-lshort-french
Version:	5.01fr.0
Release:	1
Summary:	Short introduction to LaTeX, French translation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-french.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
