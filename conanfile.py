from conans import ConanFile, CMake, tools
from six import StringIO

class SimpleWebServerConan(ConanFile):
    name = "Simple-Web-Server"
    version = "3.1.1"
    license = "https://gitlab.com/eidheim/Simple-Web-Server/-/blob/master/LICENSE"
    url = "https://gitlab.com/eidheim/Simple-Web-Server"
    description = "A very simple, fast, multithreaded, platform independent HTTP and HTTPS server and client library implemented using C++11 and Boost.Asio. Created to be an easy way to make REST resources available from C++ applications."
    options = {"openssl": [True, False]}
    default_options = {
        "openssl": True, 
        "boost:without_contract": True, 
        "boost:without_fiber": True, 
        "boost:without_graph": True, 
        "boost:without_log": True,
        "boost:without_json": True,
        "boost:without_locale": True,
        "boost:without_wave": True,
        "boost:without_math": True,
        "boost:without_nowide": True,
        "boost:without_program_options": True
    }
    requires = "boost/[>=1.53.0]" 
    generators = "cmake"
    exports_sources = "*"    
    source_url = "https://gitlab.com/eidheim/Simple-Web-Server.git"
    source_subfolder = "Simple-Web-Server"

    def source(self):
        self.run("git clone " + self.source_url)

        with tools.chdir(self.source_subfolder):
            version_tag = "v{0}".format(self.version)
            tag_info = StringIO()
            self.run("git tag -l {0}".format(version_tag), output=tag_info)
            if len(tag_info.getvalue().strip()) != 0:
                self.run("git checkout " + version_tag)
            else:
                self.run("git checkout master")

    def config_options(self):
        if self.options.openssl:
            self.requires("openssl/1.1.1k")

    def configure(self):
        self.options["boost"].without_test = True

    def package_id(self):
        self.info.header_only()
        
    def package(self):
        self.copy("*.h", dst="include", src=self.source_subfolder)
        self.copy("*.hpp", dst="include", src=self.source_subfolder)
        self.copy("LICENSE", dst="licenses", src=self.source_subfolder)

