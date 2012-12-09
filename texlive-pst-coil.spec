# revision 24020
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-coil
# catalog-date 2011-09-19 17:03:12 +0200
# catalog-license lppl
# catalog-version 1.06
Name:		texlive-pst-coil
Version:	1.06
Release:	2
Summary:	A PSTricks package for coils, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-coil
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-coil.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-coil.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-coil.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-coil is a PSTricks based package for coils and zigzags and
for coil and zigzag node connections.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-coil/pst-coil.pro
%{_texmfdistdir}/tex/generic/pst-coil/pst-coil.tex
%{_texmfdistdir}/tex/latex/pst-coil/pst-coil.sty
%doc %{_texmfdistdir}/doc/generic/pst-coil/Changes
%doc %{_texmfdistdir}/doc/generic/pst-coil/README
%doc %{_texmfdistdir}/doc/generic/pst-coil/pst-coil-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-coil/pst-coil-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-coil/pst-coil-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-coil/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.06-2
+ Revision: 755228
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.06-1
+ Revision: 719340
- texlive-pst-coil
- texlive-pst-coil
- texlive-pst-coil
- texlive-pst-coil

