# revision 23332
# category Package
# catalog-ctan /info/lshort/french
# catalog-date 2011-06-16 20:49:53 +0200
# catalog-license gpl
# catalog-version 5.01fr-0
Name:		texlive-lshort-french
Version:	5.01fr0
Release:	1
Summary:	Short introduction to LaTeX, French translation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-french.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.01-2
+ Revision: 753470
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.01-1
+ Revision: 718890
- texlive-lshort-french
- texlive-lshort-french
- texlive-lshort-french
- texlive-lshort-french

