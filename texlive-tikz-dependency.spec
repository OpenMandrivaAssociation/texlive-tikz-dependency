# revision 24700
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-dependency
# catalog-date 2011-11-29 12:27:25 +0100
# catalog-license nosource
# catalog-version 1.0
Name:		texlive-tikz-dependency
Version:	1.0
Release:	1
Summary:	A library for drawing dependency graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-dependency
License:	NOSOURCE
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

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-dependency/tikz-dependency.sty
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/AUTHORS
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/LICENSE
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/README
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual-en-macros.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual.code.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual.pdflinks.code.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual.prettyprinter.code.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/tikz-dependency-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/tikz-dependency-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
