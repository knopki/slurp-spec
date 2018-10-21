%global provider        github
%global provider_tld    com
%global project         emersion
%global repo            slurp
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          d907d308eb1eebf9b1be4a047edbc8f163bdd4b7
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           slurp
Version:        0.0.1
Release:        4.git%{shortcommit}%{?dist}
Summary:        Select a region in a Wayland compositor and print it to the standard output.
License:        MIT
URL:            https://%{provider_prefix}

Source:         https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

Requires:       libwayland-client
Requires:       cairo
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cairo-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  scdoc

%description
%{summary}.

%prep
%setup -q -n %{repo}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/slurp
%{_mandir}/man1/slurp.1.gz

%changelog
* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-4.gitd907d30
- Fix dependency

* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-3.gitd907d30
- Fix dependency

* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-2.gitd907d30
- Fix dependency

* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-1.gitd907d30
- Initial package
