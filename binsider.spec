%undefine _debugsource_packages

Name:           binsider
Version:        0.2.0
Release:        1
Summary:        Analyze ELF binaries
License:        Apache-2.0 OR MIT
Group:          Utility
URL:            https://binsider.dev/
Source0:        https://github.com/orhun/binsider/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging

%description
Binsider can perform static and dynamic analysis, inspect strings, examine
linked libraries, and perform hexdumps, within a terminal user interface.

%prep
%autosetup -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%cargo_build

%install
# no install scheme, install files manually
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
