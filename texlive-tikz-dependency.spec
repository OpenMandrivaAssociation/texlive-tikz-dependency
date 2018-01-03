Name:		texlive-tikz-dependency
Version:	1.2
Release:	1
Summary:	A library for drawing dependency graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-dependency
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dependency.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dependency.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a library that draws together existing
TikZ facilities to make a comfortable environment for drawing
dependency graphs. Basic facilities of the package include a
lot of styling facilities, to let you personalize the look and
feel of the graphs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-dependency
%doc %{_texmfdistdir}/doc/latex/tikz-dependency

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
