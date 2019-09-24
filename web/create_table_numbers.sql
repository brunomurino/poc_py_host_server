CREATE TABLE IF NOT EXISTS numbers (
    id int(11) NOT NULL AUTO_INCREMENT,
    a int(11) NOT NULL,
    b int(11) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
-- Testing
INSERT INTO numbers (a, b) VALUES (2, 4); -- First insert