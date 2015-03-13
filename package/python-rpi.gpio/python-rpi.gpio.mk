################################################################################
#
# python-rpi.gpio
#
################################################################################

PYTHON_RPI_GPIO_VERSION = 0.5.11
PYTHON_RPI_GPIO_SOURCE = RPi.GPIO-$(PYTHON_RPI_GPIO_VERSION).tar.gz
PYTHON_RPI_GPIO_SITE = https://pypi.python.org/packages/source/R/RPi.GPIO/
PYTHON_RPI_GPIO_SETUP_TYPE = distutils
PYTHON_RPI_GPIO_LICENSE = GPLv2+
PYTHON_RPI_GPIO_LICENSE_FILES = COPYING

$(eval $(python-package))
