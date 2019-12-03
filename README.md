# Python Extension Module using SWIG

- Serves as a template for creating new extension modules in C
- This example uses libcrypto from OpenSSL written in C to perform sha256()
- Alter setup.py if you want to include other static/dynamic C libraries

## Installation
    sudo ./setup.sh

## Run
    python3
    >>> import hashmodule
    >>> hashmodule.sha256('This is my message')
    '3\x11\udcb7\udcc0\udcbd\udc91\udcb6\udcc7:8!-\udce8\udcad\udce3\x1cQ\udc91\x0f\x17H\n\udcd2\x12\udced+\udc97\udc98\udca3[wG'

