from measure.measure import Measure
import abc

class IBaroDevice(abc.ABC):

	@abc.abstractmethod
	def initialize(self):
		pass

	@abc.abstractproperty
	def ready(self) -> bool:
		pass

	@abc.abstractmethod
	def read_pressure(self) -> Measure:
		pass
