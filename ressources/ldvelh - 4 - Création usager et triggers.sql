CREATE USER IF NOT EXISTS 'joueur' IDENTIFIED BY '4444';

GRANT SELECT, INSERT,DELETE
ON ldvelh.*
TO joueur;

DELIMITER $$

CREATE TRIGGER texte_vide
    BEFORE INSERT 
    ON chapitre FOR EACH ROW
    BEGIN
		
        IF chapitre.texte = NULL THEN SIGNAL SQLSTATE "03000" SET MESSAGE_TEXT = "Un chapitre doit obligatoirement contenir un texte.";
       
        END IF;

    END
    
DELIMITER ;

DELIMITER $$

CREATE TRIGGER sauvegarde_sans_fiche
    BEFORE INSERT 
    ON sauvegarde FOR EACH ROW
    BEGIN
		
        IF sauvegarde.id_fiche  = NULL THEN SIGNAL SQLSTATE "03000" SET MESSAGE_TEXT = "Vous ne pouvez pas sauvegarder une partie sans une fiche de personnage.";
       
        END IF;

    END
    
DELIMITER ;

