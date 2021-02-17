test="abcded,defdf,ghi"
test=test.replace(",","+")
print(test)
jsonvar = '{"sourceTable":"<tableName>","stColumnList":"<columnListCommaSeparated">,"targetTable":"<tableName>","ttColumnList":"<columnListCommaSeparated">}'
item = jsonvar.loads(jsonvar)
print(item.sourceTable)