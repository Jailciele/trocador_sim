from optparse import Option
from pydantic import validate_arguments, Field, root_validator, validator
from typing import Optional
from .constantes import Q_, Unit
from .base import BaseConversor


class BalancoEnergiaGlobalArgs(BaseConversor):
    q: Optional[Unit] = Field(None, description="Balanço de energia")
    m: Optional[Unit] = Field(None, description="Massa específica")
    cp: Optional[Unit] = Field(None)
    temperatura_entrada: Optional[Unit] = Field(None)
    temperatura_saida: Optional[Unit] = Field(None)

    @validator("q")
    def q_conversor(cls, value):
        if value:
            value = Q_(value, "W")
        return value

    @validator("m")
    def m_conversor(cls, value):
        if value:
            value = Q_(value, "kg/s")
        return value

    @validator("cp")
    def cp_conversor(cls, value):
        if value:
            value = Q_(value, "J/(kg*degK)")
        return value

    @validator("temperatura_entrada", "temperatura_saida")
    def temperatura_conversor(cls, value):
        if value:
            value = Q_(value, "degC")
        return value


class BalancoEnergiaGlobal:
    @validate_arguments
    def __init__(self, args: BalancoEnergiaGlobalArgs) -> None:
        self.__args = args

    @property
    def m(self) -> Q_:
        if self.__args.m is None:
            self.__args.m = self.q / (
                self.cp * (self.temperatura_entrada - self.temperatura_saida)
            )
        return self.__args.m

    @property
    def cp(self) -> Q_:
        if self.__args.cp is None:
            self.__args.cp = self.q / (
                self.m * (self.temperatura_entrada - self.temperatura_saida)
            )
        return self.__args.cp

    @property
    def temperatura_entrada(self) -> Q_:
        if self.__args.temperatura_entrada is None:
            self.__args.temperatura_entrada = (
                self.q / (self.m * self.cp)
            ) + self.temperatura_saida.to("degK")
        return self.__args.temperatura_entrada

    @property
    def temperatura_saida(self) -> Q_:
        if self.__args.temperatura_saida is None:
            self.__args.temperatura_saida = (
                self.q / (self.m * self.cp)
            ) + self.temperatura_entrada.to("degK")
        return self.__args.temperatura_saida

    @property
    def q(self) -> Q_:
        if self.__args.q is None:
            self.__args.q = (
                self.m * self.cp * (self.temperatura_entrada - self.temperatura_saida)
            )
        return self.__args.q
