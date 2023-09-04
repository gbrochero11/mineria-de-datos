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
    
    def findAll(self):
        sql = ("select ENTIDAD, Fallecidos, Tramo, Nombre, Latitud, Longitud, Municipio, Departamento from sectores_criticos_de_siniestralidad_vial_csv scdsvc")
        cnx = self.mySqlConnector.connect()
        cursor = cnx.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        data = []
        data.append(["Entidad", "Fallecidos", "Tramo", "Nombre", "Latitud", "Longitud", "Municipio", "Departamento"])
        for row in result_set:
            rowData = []
            rowData.append(row[0])
            rowData.append(row[1])
            rowData.append(row[2])
            rowData.append(row[3])
            rowData.append(row[4])
            rowData.append(row[5])
            rowData.append(row[6])
            data.append(rowData)
        cursor.close()
        cnx.close()
        return data
