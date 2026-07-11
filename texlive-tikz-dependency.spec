%global tl_name tikz-dependency
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A library for drawing dependency graphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-dependency
License:	lppl1.3c gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dependency.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dependency.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a library that draws together existing TikZ
facilities to make a comfortable environment for drawing dependency
graphs. Basic facilities of the package include a lot of styling
facilities, to let you personalize the look and feel of the graphs.

