%define upstream_name    Task-Dist-Zilla
%define upstream_version 1.102470

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Task to install dist-zilla and all its plugins
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Task/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Plugin::ApacheTest)
BuildRequires: perl(Dist::Zilla::Plugin::ArchiveRelease)
BuildRequires: perl(Dist::Zilla::Plugin::AssertOS)
BuildRequires: perl(Dist::Zilla::Plugin::Author::KENTNL::DistINI)
BuildRequires: perl(Dist::Zilla::Plugin::AutoVersion::Relative)
BuildRequires: perl(Dist::Zilla::Plugin::Bootstrap::lib)
BuildRequires: perl(Dist::Zilla::Plugin::Bugtracker)
BuildRequires: perl(Dist::Zilla::Plugin::BumpVersionFromGit)
BuildRequires: perl(Dist::Zilla::Plugin::CSJEWELL::AuthorTest)
BuildRequires: perl(Dist::Zilla::Plugin::CSJEWELL::BeforeBuild)
BuildRequires: perl(Dist::Zilla::Plugin::CSJEWELL::DotFileFix)
BuildRequires: perl(Dist::Zilla::Plugin::CSJEWELL::FTPUploadToOwnSite)
BuildRequires: perl(Dist::Zilla::Plugin::CSJEWELL::SubversionDist)
BuildRequires: perl(Dist::Zilla::Plugin::CSJEWELL::VersionGetter)
BuildRequires: perl(Dist::Zilla::Plugin::Catalyst)
BuildRequires: perl(Dist::Zilla::Plugin::Catalyst::Helper)
BuildRequires: perl(Dist::Zilla::Plugin::Catalyst::New)
BuildRequires: perl(Dist::Zilla::Plugin::ChangelogFromGit)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangesHasContent)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangesTests)
BuildRequires: perl(Dist::Zilla::Plugin::CheckExtraTests)
BuildRequires: perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires: perl(Dist::Zilla::Plugin::ConsistentVersionTest)
BuildRequires: perl(Dist::Zilla::Plugin::CopyReadmeFromBuild)
BuildRequires: perl(Dist::Zilla::Plugin::CopyTo)
BuildRequires: perl(Dist::Zilla::Plugin::CriticTests)
BuildRequires: perl(Dist::Zilla::Plugin::DistManifestTests)
BuildRequires: perl(Dist::Zilla::Plugin::DualBuilders)
BuildRequires: perl(Dist::Zilla::Plugin::DynamicManifest)
BuildRequires: perl(Dist::Zilla::Plugin::EOLTests)
BuildRequires: perl(Dist::Zilla::Plugin::FatPacker)
BuildRequires: perl(Dist::Zilla::Plugin::Git)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Check)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Commit)
BuildRequires: perl(Dist::Zilla::Plugin::Git::CommitBuild)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Init)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Push)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Tag)
BuildRequires: perl(Dist::Zilla::Plugin::GitFmtChanges)
BuildRequires: perl(Dist::Zilla::Plugin::GitObtain)
BuildRequires: perl(Dist::Zilla::Plugin::GitVersionCheckCJM)
BuildRequires: perl(Dist::Zilla::Plugin::GithubMeta)
BuildRequires: perl(Dist::Zilla::Plugin::HasVersionTests)
BuildRequires: perl(Dist::Zilla::Plugin::Homepage)
BuildRequires: perl(Dist::Zilla::Plugin::InlineFilesMARCEL)
BuildRequires: perl(Dist::Zilla::Plugin::InstallGuide)
BuildRequires: perl(Dist::Zilla::Plugin::KwaliteeTests)
BuildRequires: perl(Dist::Zilla::Plugin::LatestPrereqs)
BuildRequires: perl(Dist::Zilla::Plugin::LocaleMsgfmt)
BuildRequires: perl(Dist::Zilla::Plugin::MakeMaker::Awesome)
BuildRequires: perl(Dist::Zilla::Plugin::MakeMaker::SkipInstall)
BuildRequires: perl(Dist::Zilla::Plugin::MatchManifest)
BuildRequires: perl(Dist::Zilla::Plugin::Mercurial)
BuildRequires: perl(Dist::Zilla::Plugin::Mercurial::Check)
BuildRequires: perl(Dist::Zilla::Plugin::Mercurial::Push)
BuildRequires: perl(Dist::Zilla::Plugin::Mercurial::Tag)
BuildRequires: perl(Dist::Zilla::Plugin::MetaData::BuiltWith)
BuildRequires: perl(Dist::Zilla::Plugin::MetaData::BuiltWith::All)
BuildRequires: perl(Dist::Zilla::Plugin::MetaNoIndex)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::Class)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::FromFile)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::Package)
BuildRequires: perl(Dist::Zilla::Plugin::MetaRecommends)
BuildRequires: perl(Dist::Zilla::Plugin::MinimumPerl)
BuildRequires: perl(Dist::Zilla::Plugin::MinimumVersionTests)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleBuild::Custom)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleBuild::XSOrPP)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleInstall)
BuildRequires: perl(Dist::Zilla::Plugin::NoAutomatedTesting)
BuildRequires: perl(Dist::Zilla::Plugin::NoTabsTests)
BuildRequires: perl(Dist::Zilla::Plugin::OurPkgVersion)
BuildRequires: perl(Dist::Zilla::Plugin::PerlTidy)
BuildRequires: perl(Dist::Zilla::Plugin::PodLoom)
BuildRequires: perl(Dist::Zilla::Plugin::PodPurler)
BuildRequires: perl(Dist::Zilla::Plugin::PodSpellingTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires: perl(Dist::Zilla::Plugin::Prepender)
BuildRequires: perl(Dist::Zilla::Plugin::ProgCriticTests)
BuildRequires: perl(Dist::Zilla::Plugin::PurePerlTests)
BuildRequires: perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires: perl(Dist::Zilla::Plugin::ReadmeMarkdownFromPod)
BuildRequires: perl(Dist::Zilla::Plugin::ReportVersions)
BuildRequires: perl(Dist::Zilla::Plugin::ReportVersions::Tiny)
BuildRequires: perl(Dist::Zilla::Plugin::Repository)
BuildRequires: perl(Dist::Zilla::Plugin::Rsync)
BuildRequires: perl(Dist::Zilla::Plugin::SVK)
BuildRequires: perl(Dist::Zilla::Plugin::SVK::Check)
BuildRequires: perl(Dist::Zilla::Plugin::SVK::Commit)
BuildRequires: perl(Dist::Zilla::Plugin::SVK::Push)
BuildRequires: perl(Dist::Zilla::Plugin::SVK::Tag)
BuildRequires: perl(Dist::Zilla::Plugin::Signature)
BuildRequires: perl(Dist::Zilla::Plugin::SubmittingPatches)
BuildRequires: perl(Dist::Zilla::Plugin::SurgicalPkgVersion)
BuildRequires: perl(Dist::Zilla::Plugin::SurgicalPodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::SvnObtain)
BuildRequires: perl(Dist::Zilla::Plugin::SynopsisTests)
BuildRequires: perl(Dist::Zilla::Plugin::TaskWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::TemplateCJM)
BuildRequires: perl(Dist::Zilla::Plugin::TemplateFiles)
BuildRequires: perl(Dist::Zilla::Plugin::Twitter)
BuildRequires: perl(Dist::Zilla::Plugin::UnusedVarsTests)
BuildRequires: perl(Dist::Zilla::Plugin::UpdateGitHub)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromModule)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromPrev)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromPrev::Finder::Git::LastVersion)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromPrev::Style::Classic)
BuildRequires: perl(Dist::Zilla::PluginBundle::AVAR)
BuildRequires: perl(Dist::Zilla::PluginBundle::BINGOS)
BuildRequires: perl(Dist::Zilla::PluginBundle::CJM)
BuildRequires: perl(Dist::Zilla::PluginBundle::CSJEWELL)
BuildRequires: perl(Dist::Zilla::PluginBundle::FAYLAND)
BuildRequires: perl(Dist::Zilla::PluginBundle::Git)
BuildRequires: perl(Dist::Zilla::PluginBundle::IDOPEREL)
BuildRequires: perl(Dist::Zilla::PluginBundle::JQUELIN)
BuildRequires: perl(Dist::Zilla::PluginBundle::KENTNL)
BuildRequires: perl(Dist::Zilla::PluginBundle::KENTNL::Lite)
BuildRequires: perl(Dist::Zilla::PluginBundle::MARCEL)
BuildRequires: perl(Dist::Zilla::PluginBundle::Mercurial)
BuildRequires: perl(Dist::Zilla::PluginBundle::PDONELAN)
BuildRequires: perl(Dist::Zilla::PluginBundle::RJBS)
BuildRequires: perl(Dist::Zilla::PluginBundle::ROKR)
BuildRequires: perl(Dist::Zilla::PluginBundle::ROKR::Basic)
BuildRequires: perl(Dist::Zilla::PluginBundle::Rakudo)
BuildRequires: perl(Dist::Zilla::PluginBundle::SVK)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This task is merely a placeholder to pull all dist-zilla related modules in
one go.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
