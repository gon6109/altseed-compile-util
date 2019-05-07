import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../Altseed/Script'))

import aceutils

aceutils.cdToScript()

with aceutils.CurrentDir('..'):
    aceutils.call(r'git submodule update --init --recursive')
    aceutils.call(r'python Script\build_ap.py --vs2019')
    aceutils.call(r'python Script\build_ar.py --vs2019')
    aceutils.call(r'python Script\build_Box2D.py --vs2019')
    aceutils.call(r'python Script\build_bullet.py --vs2019')
    aceutils.call(r'python Script\build_culling2d.py --vs2019')
    aceutils.call(r'python Script\build_culling3d.py --vs2019')
    aceutils.call(r'python Script\build_effekseer.py --vs2019')
    aceutils.call(r'python Script\build_freetype.py --vs2019')
    aceutils.call(r'python Script\build_glew.py --vs2019')
    aceutils.call(r'python Script\build_glfw.py --vs2019')
    aceutils.call(r'python Script\build_gtest.py --vs2019')
    aceutils.call(r'python Script\build_libgd.py --vs2019')
    aceutils.call(r'python Script\build_libpng.py --vs2019')
    aceutils.call(r'python Script\build_OpenSoundMixer.py --vs2019')
    aceutils.call(r'python Dev\generateCoreToEngineHeader.py')
    aceutils.call(r'python Dev\generateEngineHeader.py')
    aceutils.call(r'python Dev\generate_swig.py')
    aceutils.call(r'python Script\export_doxygen_core.py')
    aceutils.call(r'python Script\generateSwigWrapper.py')
