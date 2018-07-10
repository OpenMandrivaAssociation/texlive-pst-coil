Name:		texlive-pst-coil
Version:	1.07
Release:	2
Summary:	A PSTricks package for coils, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-coil
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-coil.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-coil.doc.tar.xz
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
%{_texmfdistdir}/dvips/pst-coil
%{_texmfdistdir}/tex/generic/pst-coil
%{_texmfdistdir}/tex/latex/pst-coil
%doc %{_texmfdistdir}/doc/generic/pst-coil

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
