import core.MySqlConnection as MySqlConnection
from models.dataSet import DataSet


class DataSETRepository(object):
    def __init__(self):
        self.mySqlConnector = MySqlConnection.MySQLConnector()

    def register(self, data: DataSet):
        sql = ("INSERT INTO sectores_criticos_de_siniestralidad_vial_csv  "
               "(ENTIDAD, Fallecidos, Nombre, Latitud, Longitud, PR, Municipio, Departamento) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cnx = self.mySqlConnector.connect()
        cursor = cnx.cursor()
        cursor.execute(sql, (data.entidad, data.fallecidos, data.nombre,
                       data.latitud, data.longitud, data.pr, data.municipio, data.departamento))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
