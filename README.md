# ConanFile for Simple-Web-Server
See https://gitlab.com/eidheim/Simple-Web-Server for more information on the library.

# Building and Uploading

```
conan create . --build
conan upload --force -c "simple-web-server/*" -r <your-remote>
```

# Using in CMake
```
conan_cmake_configure(REQUIRES Simple-Web-Server/2.2.6 GENERATORS cmake_find_package)
...

find_package(Simple-Web-Server REQUIRED)
...
```
