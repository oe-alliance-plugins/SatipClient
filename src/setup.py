from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.SatipClient'
setup(name='enigma2-plugin-systemplugins-satipclient',
       version='3.0',
       description='Satip Client',
       package_dir={pkg: 'SatipClient'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'keymap.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
